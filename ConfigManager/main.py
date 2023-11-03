import validators
from config import write_config, DEFAULT_CONFIG_FILE_PATH


config = {
    'raspi_ip': None,
    'raspi_port': None,
    'unity_ip': None,
    'unity_port': None
}
config_validate = {
    'raspi_ip': validators.validate_ip,
    'raspi_port': validators.validate_port,
    'unity_ip': validators.validate_ip,
    'unity_port': validators.validate_port
}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_write = True
    for key in config.keys():
        var = input(f'Enter {key}: ')
        var = config_validate[key](var)
        if var:
            config[key] = var
        else:
            print('Invalid input')
            do_write = False
            break

    if do_write:
        print('Writing config to: %s' % DEFAULT_CONFIG_FILE_PATH)
        write_config(config)
