from subprocess import run, PIPE

import os
import pytest

B_FILE_PATH = '/bin/ip_tools'

if os.path.isfile(B_FILE_PATH):
    def test_src_folder_containts_ip_check():
        assert os.path.isfile(B_FILE_PATH)

    def test_ip_tools_error_input_1():
        result = run([B_FILE_PATH], input='0\n128.0.10.2', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_ip_tools_error_input_2():
        result = run([B_FILE_PATH], input='a\n128.0.10.2', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr
    
    def test_ip_tools_error_input_3():
        result = run([B_FILE_PATH], input='0.4\n128.0.10.2', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_ip_tools_error_input_4():
        result = run([B_FILE_PATH], input='1\nabs.0.10.2', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_ip_tools_error_input_5():
        result = run([B_FILE_PATH], input='1\n128.0.10.2a', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr
    
    def test_ip_tools_error_input_6():
        result = run([B_FILE_PATH], input='1\n128.0a.10.2', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr
    
    def test_ip_tools_error_input_7():
        result = run([B_FILE_PATH], input='1\n128.0.10a.2', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_ip_tools_error_input_8():
        result = run([B_FILE_PATH], input='2\n128.0.10.2\n\n128.0.10a.2', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_ip_tools_error_input_8():
        result = run([B_FILE_PATH], input='2\n128.0.10.2\n\n128.0.10.2a', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_ip_tools_invalid_input_1():
        result = run([B_FILE_PATH], input='1\n256.0.0.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_tools_invalid_input_2():
        result = run([B_FILE_PATH], input='1\n999.999.999.999', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_tools_invalid_input_3():
        result = run([B_FILE_PATH], input='1\n001.0.0.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_tools_invalid_input_4():
        result = run([B_FILE_PATH], input='1\n1.0.0.1000', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'
    
    def test_ip_tools_invalid_input_5():
        result = run([B_FILE_PATH], input='1\n0.1234.0.0', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'INVALID'

    def test_ip_tools_invalid_input_6():
        result = run([B_FILE_PATH], input='2\n128.0.0.1\n128.0.10.2', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'
    
    def test_ip_tools_invalid_input_7():
        result = run([B_FILE_PATH], input='2\n0.0.0.1\n0.0.1.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'

    def test_ip_tools_invalid_input_8():
        result = run([B_FILE_PATH], input='2\n128.128.127.1\n128.128.128.3', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'
    
    def test_ip_tools_invalid_input_9():
        result = run([B_FILE_PATH], input='2\n100.200.0.1\n100.200.1.25', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'NO'

    def test_ip_tools_valid_input_1():
        result = run([B_FILE_PATH], input='1\n192.168.0.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'
    
    def test_ip_tools_valid_input_2():
        result = run([B_FILE_PATH], input='1\n255.255.255.255', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'

    def test_ip_tools_valid_input_3():
        result = run([B_FILE_PATH], input='1\n0.0.0.0', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'
    
    def test_ip_tools_valid_input_4():
        result = run([B_FILE_PATH], input='1\n66.128.234.1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'VALID'

    def test_ip_tools_valid_input_5():
        result = run([B_FILE_PATH], input='2\n100.200.1.1\n100.200.1.25', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'
    
    def test_ip_tools_valid_input_6():
        result = run([B_FILE_PATH], input='2\n1.1.1.1\n1.1.1.2', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'
    
    def test_ip_tools_valid_input_7():
        result = run([B_FILE_PATH], input='2\n255.255.255.1\n255.255.255.0', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'
    
    def test_ip_tools_valid_input_8():
        result = run([B_FILE_PATH], input='2\n12.24.55.0\n12.24.55.255', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == 'YES'

if __name__ == '__main__':
    pytest.main()