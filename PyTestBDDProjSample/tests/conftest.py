def pytest_bdd_after_scenario(request, feature, scenario):
    print('====After scenario hook executed')
    # print(f'{scenario}')

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print('====This failed')
    print(f'step failed : {step}')
    # print(f'{scenario}')
    # print(f'{step}')