import os

curr_dirpath = os.path.dirname(os.path.abspath(__file__))
with open(curr_dirpath+'/config/path_config.ini', 'wb') as f:
    f.write('[PATHS]\n')
    f.write('base_dirpath:%s\n'%curr_dirpath)
    f.write('src_dirpath:%(base_dirpath)s/src/\n')
    f.write('raw_data_dirpath:%(base_dirpath)s/data/raw\n')
    f.write('int_data_dirpath:%(base_dirpath)s/data/intermediate\n')
    f.write('models_dirpath:%(base_dirpath)s/models\n')
    f.write('results_dirpath:%(base_dirpath)s/results\n')
    f.write('plots_dirpath:%(base_dirpath)s/results/plots\n')
    f.write('logging_dirpath:%(base_dirpath)s/logging\n')
    f.write('test_dirpath:%(base_dirpath)s/tests\n')
