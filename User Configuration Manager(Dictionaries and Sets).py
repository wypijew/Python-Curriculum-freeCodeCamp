test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high",
    "language": "en"
}

def add_setting(settings: dict, setting: tuple) -> str:
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."        
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, setting: tuple) -> str:
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings: dict, key: str) -> str:
    key = key.lower()
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."

    result = "Current User Settings:"
    for key, value in settings.items():
        result += f"\n{key.capitalize()}: {value}"
    result += '\n'
    
    return result