# This file is generated by ConfigPorperties.generator.py, do not modify this file directly.
import os
from typing import List, Any, Dict

class Report:
    def __init__(self) -> None:
        # ==================================================================================================
        # Just paste it into `ConfigManager.__init__()`
        
        self.defaults_SHA256 = "4c937f50a444b1297075a9b77f178e10103733e8114bac703169dcd9a82215d9"
        
        self.config_files: Dict[str, str] = {
            "basic": os.path.join(self.config_folder, "basic.json"),
            "info_layout": os.path.join(self.config_folder, "info_layout.json")
        }
        self.config_schema_files: Dict[str, str] = {
            "basic": os.path.join(self.config_schema_folder, "basic.schema.json"),
            "info_layout": os.path.join(self.config_schema_folder, "info_layout.schema.json")
        }

        # ==================================================================================================
        # Just paste it into `ConfigManager._load_config()`

        if self.active_configfile == os.path.join(self.config_folder, "basic.json"):
            self.font_file: str = self.config.get('font_file', None)  # Path to the primary font file.
            self.font_file_2: str = self.config.get('font_file_2', None)  # Path to the secondary font file.
            self.logo_file: str = self.config.get('logo_file', None)  # Path to the logo image file.
            self.resize_scale: int = self.config.get('resize_scale', None)  # Scaling factor for resizing.
            self.avoid_leading: bool = self.config.get('avoid_leading', None)  # Indicates whether to avoid leading content.
            self.avoid_ending: bool = self.config.get('avoid_ending', None)  # Indicates whether to avoid ending content.
            self.grid_size: List[Any] = self.config.get('grid_size', None)  # Grid size configuration, represented as an array of two integers.

        if self.active_configfile == os.path.join(self.config_folder, "info_layout.json"):
            self.fonts: List[Dict[str, str]] = self.config.get('fonts', None)  # 
            self.font_list: List[int] = self.config.get('font_list', None)  # 
            self.time_font: int = self.config.get('time_font', None)  # 
            self.horizontal_spacing: int = self.config.get('horizontal_spacing', None)  # 
            self.vertical_spacing: int = self.config.get('vertical_spacing', None)  # 
            self.content_margin_left: int = self.config.get('content_margin_left', None)  # 
            self.content_margin_top: int = self.config.get('content_margin_top', None)  # 
            self.title_margin_left: int = self.config.get('title_margin_left', None)  # 
            self.title_margin_top: int = self.config.get('title_margin_top', None)  # 
            self.shade_offset: List[int] = self.config.get('shade_offset', None)  # 
            self.text_color: List[int] = self.config.get('text_color', None)  # 
            self.shade_color: List[int] = self.config.get('shade_color', None)  # 
            self.text_list: List[List[Dict[str, str] | str]] = self.config.get('text_list', None)  # 
            self.pos_list: List[List[int]] = self.config.get('pos_list', None)  # 
