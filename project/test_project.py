from project import (
        get_ws,
        sample_type_checker,
        sample_unit_checker,
        sample_limit_checker,
        sample_appearance_checker,
        sample_analyte_checker,
        sample_ar_rt_checker,
        sample_ar_cc_checker,
        sample_other_checker,
)
import pytest


def main():
    test_get_ws()
    test_sample_type_checker()
    test_sample_unit_checker()
    test_sample_limit_checker()
    test_sample_appearance_checker_string()
    test_sample_appearance_checker_int()
    test_sample_analyte_checker()
    test_sample_ar_rt_checker()
    test_sample_ar_cc_checker()
    test_sample_other_checker_string()
    test_sample_other_checker_int()
    ...


def test_get_ws():
    with pytest.raises(SystemExit):
        get_ws('./Cleaning Samples Template.x')


def test_sample_type_checker():
    with pytest.raises(SystemExit):
        sample_type_checker([{
                'Sample ID': 'Test String Here',
                'Sample Type': 'THIS SHOULD CAUSE TEST TO EXIT',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'pass',
                'Analyte': 'Test String Here',
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            }])


def test_sample_unit_checker():
    with pytest.raises(SystemExit):
        sample_unit_checker([{
                'Sample ID': 'Test String Here',
                'Sample Type': 'sample',
                'Units': 28,
                'Limit': 23,
                'Appearance': 'pass',
                'Analyte': 'Test String Here',
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            }])


def test_sample_limit_checker():
    with pytest.raises(SystemExit):
        sample_limit_checker([{
            'Sample ID': 'Test String Here',
            'Sample Type': 'blank',
            'Units': 'ug/ml',
            'Limit': 'THIS SHOULD RAISE AN ERROR',
            'Appearance': 'pass',
            'Analyte': 'Test String Here',
            'Analyte RT': 2.10,
            'Analyte Result': 0.12,
            'Other-Peaks': None,
            }])


def test_sample_appearance_checker_string():
    with pytest.raises(SystemExit):
        sample_appearance_checker([{
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'THIS SHOULD RAISE AN ERROR',
                'Analyte': 'Test String Here',
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            }])


def test_sample_appearance_checker_int():
    with pytest.raises(SystemExit):
        sample_appearance_checker([{
            'Sample ID': 'Test String Here',
            'Sample Type': 'blank',
            'Units': 'ug/ml',
            'Limit': 23,
            'Appearance': 23,
            'Analyte': 'Test String Here',
            'Analyte RT': 2.10,
            'Analyte Result': 0.12,
            'Other-Peaks': None,
            }])


def test_sample_analyte_checker():
    with pytest.raises(SystemExit):
        sample_analyte_checker([{
            'Sample ID': 'Test String Here',
            'Sample Type': 'blank',
            'Units': 'ug/ml',
            'Limit': 23,
            'Appearance': 'pass',
            'Analyte': None,
            'Analyte RT': 2.10,
            'Analyte Result': 0.12,
            'Other-Peaks': None,
            }])


def test_sample_ar_rt_checker():
    with pytest.raises(SystemExit):
        sample_ar_rt_checker([{
            'Sample ID': 'Test String Here',
            'Sample Type': 'blank',
            'Units': 'ug/ml',
            'Limit': 23,
            'Appearance': 'pass',
            'Analyte': 'Test string here',
            'Analyte RT': 'THIS SHOULD RAISE A ERROR',
            'Analyte Result': 0.12,
            'Other-Peaks': None,
            }])


def test_sample_ar_cc_checker():
    with pytest.raises(SystemExit):
        sample_ar_cc_checker([{
            'Sample ID': 'Test String Here',
            'Sample Type': 'blank',
            'Units': 'ug/ml',
            'Limit': 23,
            'Appearance': 'pass',
            'Analyte': 'Test string here',
            'Analyte RT': 2.22,
            'Analyte Result': 'THIS SHOULD RAISE AN ERROR',
            'Other-Peaks': None,
            }])


def test_sample_other_checker_string():
    with pytest.raises(SystemExit):
        sample_other_checker([{
            'Sample ID': 'Test String Here',
            'Sample Type': 'blank',
            'Units': 'ug/ml',
            'Limit': 23,
            'Appearance': 'pass',
            'Analyte': 'Test string here',
            'Analyte RT': 2.22,
            'Analyte Result': 34,
            'Other-Peaks': 'THIS SHOULD RAISE AN ERROR',
            }])


def test_sample_other_checker_int():
    with pytest.raises(SystemExit):
        sample_other_checker([{
            'Sample ID': 'Test String Here',
            'Sample Type': 'blank',
            'Units': 'ug/ml',
            'Limit': 23,
            'Appearance': 'pass',
            'Analyte': 'Test string here',
            'Analyte RT': 2.22,
            'Analyte Result': 34,
            'Other-Peaks': 28,
            }])


if __name__ == '__main__':
    main()
