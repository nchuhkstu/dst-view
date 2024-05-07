import configparser

config = configparser.ConfigParser()
config.read('cluster_path.ini')
cluster_path = config.get('cluster', 'cluster_path')
