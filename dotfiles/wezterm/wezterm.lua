-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices

-- For example, changing the color scheme:
config.color_scheme = "Catpucchin Mocha"

config.font = wezterm.font("JetBrains Mono")
-- config.font = wezterm.font("MesloLGS Nerd Font Mono")

-- Set the font size to 16 points
config.font_size = 16

-- Move the tab bar to the bottom
config.tab_bar_at_bottom = true
config.use_fancy_tab_bar = true

config.window_background_opacity = 0.9
config.macos_window_background_blur = 10
config.window_decorations = "RESIZE"

local act = wezterm.action

config.keys = {
	{
		key = "t",
		mods = "CMD|SHIFT",
		action = act.ShowTabNavigator,
	},
	-- other keys
}

-- and finally, return the configuration to wezterm
return config
