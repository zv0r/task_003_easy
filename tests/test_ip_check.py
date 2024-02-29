from subprocess import run, PIPE

import os
import pytest

B_FILE_PATH = '/src/ip_check'

if os.path.isfile(B_FILE_PATH):
    def test_src_folder_containts_ip_check():
        assert os.path.isfile(B_FILE_PATH)

    def test_ip_check_invalid_ip_1():
        result = run([B_FILE_PATH], input='256.0.0.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_check_invalid_ip_2():
        result = run([B_FILE_PATH], input='999.999.999.999', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_check_invalid_ip_3():
        result = run([B_FILE_PATH], input='001.0.0.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_check_invalid_ip_4():
        result = run([B_FILE_PATH], input='1.0.0.1000', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_check_invalid_ip_5():
        result = run([B_FILE_PATH], input='0.1234.0.0', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'

    def test_ip_check_valid_ip_1():
        result = run([B_FILE_PATH], input='192.168.0.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'
    
    def test_ip_check_valid_ip_2():
        result = run([B_FILE_PATH], input='255.255.255.255', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'

    def test_ip_check_valid_ip_3():
        result = run([B_FILE_PATH], input='0.0.0.0', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'
    
    def test_ip_check_valid_ip_4():
        result = run([B_FILE_PATH], input='66.128.234.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'

if __name__ == '__main__':
    pytest.main()