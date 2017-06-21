import config_default
configs = config_default.configs
def merge(x,y):
	z = x.copy()
	z.update(y)
	return z
try:
    import config_override
    #configs = merge(configs, config_override.configs)
except ImportError:
    pass