"""
Centralized logging configuration for the application
"""

import logging
import sys
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler
from typing import Optional
import threading


# 线程锁，确保全局logo创建时的线程安全
_logo_lock = threading.Lock()
_logo_instance = None


def setup_logo(
    name: Optional[str] = None,
    level: Optional[str] = None,
    format_string: Optional[str] = None,
    log_file: Optional[str] = None,
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Setup and configure a logo (logger) instance
    
    Args:
        name: Logger name (if None, defaults to root logger)
        level: Log level (DEBUG, INFO, WARN, ERROR, CRITICAL)
        format_string: Custom format string
        log_file: Log file path (if None, defaults to logs/{name}.log)
        max_bytes: Maximum size of each log file before rotation (default: 10MB)
        backup_count: Number of backup files to keep (default: 5)
        
    Returns:
        Configured logger instance
    """
    logo_instance = logging.getLogger(name)
    
    # Avoid adding multiple handlers if logo already exists
    if logo_instance.handlers:
        return logo_instance
    
    # Set log level from parameter or environment
    log_level = level or os.getenv("LOG_LEVEL", "INFO")
    logo_instance.setLevel(getattr(logging, log_level.upper()))
    
    # Create formatter
    if format_string is None:
        format_string = (
            "%(asctime)s - %(name)s - %(levelname)s - "
            "[%(filename)s:%(lineno)d] - %(message)s"
        )
    formatter = logging.Formatter(format_string)
    
    # Create console handler with UTF-8 encoding
    import io
    console_handler = logging.StreamHandler(
        io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)
    )
    console_handler.setLevel(logo_instance.level)
    console_handler.setFormatter(formatter)
    logo_instance.addHandler(console_handler)
    
    # Create file handler with rotation
    if log_file is None:
        # Create logs directory if it doesn't exist
        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)
        # 如果name为空，使用 "app.log" 作为默认文件名
        file_name = name.replace('.', '_') if name else "app"
        log_file = logs_dir / f"{file_name}.log"
    else:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
    
    file_handler = RotatingFileHandler(
        filename=str(log_file),
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setLevel(logo_instance.level)
    file_handler.setFormatter(formatter)
    logo_instance.addHandler(file_handler)
    
    return logo_instance


def get_logo() -> logging.Logger:
    """
    Get or create the global thread-safe logo instance
    
    Returns:
        Thread-safe global logger instance
    """
    global _logo_instance
    
    # 双重检查锁定模式（Double-Checked Locking）
    if _logo_instance is None:
        with _logo_lock:
            if _logo_instance is None:
                _logo_instance = setup_logo()
    
    return _logo_instance


# Global logo instance - 线程安全的延迟初始化
logo = get_logo()