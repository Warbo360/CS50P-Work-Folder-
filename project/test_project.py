from project import (
        sample_list_checker,
        get_ws,
        get_sample_data,
        state_gen,
        sample_type_checker,
        sample_limit_checker,
        sample_appearance_checker,
        sample_analyte_checker,
        sample_ar_rt_checker,
        sample_ar_cc_checker,
        sample_other_checker,
)
import pytest
from openpyxl import load_workbook  # Allows reading and writing spreadsheet files
import sys


def main():
    test_sample_type_checker()
    test_sample_limit_checker()
    test_sample_appearance_checker_string()
    test_sample_appearance_checker_int()
    test_sample_analyte_checker()
    test_sample_ar_rt_checker()
    test_sample_ar_cc_checker()
    test_sample_other_checker()
    ...


def test_sample_type_checker():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'THIS SHOULD CAUSE TEST TO EXIT',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'pass',
                'Analyte': 'Test String Here',
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            })


def test_sample_limit_checker():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 'THIS SHOULD RAISE AN ERROR',
                'Appearance': 'pass',
                'Analyte': 'Test String Here',
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            })


def test_sample_appearance_checker_string():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'THIS SHOULD RAISE AN ERROR',
                'Analyte': 'Test String Here',
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            })


def test_sample_appearance_checker_int():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 23,
                'Analyte': 'Test String Here',
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            })


def test_sample_analyte_checker():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'pass',
                'Analyte': None,
                'Analyte RT': 2.10,
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            })


def test_sample_ar_rt_checker():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'pass',
                'Analyte': 'Test string here',
                'Analyte RT': 'THIS SHOULD RAISE A ERROR',
                'Analyte Result': 0.12,
                'Other-Peaks': None,
            })


def test_sample_ar_cc_checker():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'pass',
                'Analyte': 'Test string here',
                'Analyte RT': 2.22,
                'Analyte Result': 'THIS SHOULD RAISE AN ERROR',
                'Other-Peaks': None,
            })


def test_sample_other_checker():
    with pytest.raises(TypeError):
        sample_type_checker({
                'Sample ID': 'Test String Here',
                'Sample Type': 'blank',
                'Units': 'ug/ml',
                'Limit': 23,
                'Appearance': 'pass',
                'Analyte': 'Test string here',
                'Analyte RT': 2.22,
                'Analyte Result': 34,
                'Other-Peaks': 'THIS SHOULD RAISE AN ERROR',
            })
[
        {
            'Sample ID': '100041567 LC80277',
            'Sample Type': 'blank',
            'Units': 'ug/ml', 'Limit': 1.11,
            'Appearance': 'pass',
            'Analyte': 'A-162166.0',
            'Analyte RT': 2.12,
            'Analyte Result': 20.222,
            'Other-Peaks': '(2.11, 0.13), (3.25, 0.25)'
        },
        {
            'Sample ID': '2',
            'Sample Type': 'blank',
            'Units': 'ug/100cm2',
            'Limit': 34,
            'Appearance': 'pass',
            'Analyte': 'A-162166.0',
            'Analyte RT': 2.12,
            'Analyte Result': 10,
            'Other-Peaks': '(3.46, 2.99)'
        },
        {
            'Sample ID': '3',
            'Sample Type': 'sample',
            'Units': 'ug/ml',
            'Limit': 2.12,
            'Appearance': 'fail',
            'Analyte': 'A-162166.0',
            'Analyte RT': 2.12,
            'Analyte Result': 10,
            'Other-Peaks': None
        }
]

if __name__ == '__main__':
    main()
