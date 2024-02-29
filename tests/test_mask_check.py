from subprocess import run, PIPE

import os
import pytest

B_FILE_PATH = '/src/mask_check'

if os.path.isfile(B_FILE_PATH):
    def test_src_folder_containts_ip_check():
        assert os.path.isfile(B_FILE_PATH)

    def test_mask_check_fail_1():
        result = run([B_FILE_PATH], input='128.0.0.1\n128.0.10.2', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'
    
    def test_mask_check_fail_2():
        result = run([B_FILE_PATH], input='0.0.0.1\n0.0.1.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'

    def test_mask_check_fail_3():
        result = run([B_FILE_PATH], input='128.128.127.1\n128.128.128.3', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'
    
    def test_mask_check_fail_4():
        result = run([B_FILE_PATH], input='100.200.0.1\n100.200.1.25', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'

    def test_mask_check_success_1():
        result = run([B_FILE_PATH], input='100.200.1.1\n100.200.1.25', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'
    
    def test_mask_check_success_2():
        result = run([B_FILE_PATH], input='1.1.1.1\n1.1.1.2', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'
    
    def test_mask_check_success_3():
        result = run([B_FILE_PATH], input='255.255.255.1\n255.255.255.0', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'
    
    def test_mask_check_success_4():
        result = run([B_FILE_PATH], input='12.24.55.0\n12.24.55.255', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'

if __name__ == '__main__':
    pytest.main()