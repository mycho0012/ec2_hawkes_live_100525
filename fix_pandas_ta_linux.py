"""
Linux/Ubuntu 서버용 pandas_ta 패치 스크립트
"""
import os
import sys

def fix_pandas_ta():
    # 가능한 site-packages 경로들 검색
    site_packages_paths = []
    for path in sys.path:
        if 'site-packages' in path or 'dist-packages' in path:
            site_packages_paths.append(path)
    
    # 사용자 로컬 경로 추가
    home = os.path.expanduser('~')
    for py_ver in ['3.8', '3.9', '3.10', '3.11', '3.12']:
        local_path = os.path.join(home, '.local', 'lib', f'python{py_ver}', 'site-packages')
        if os.path.exists(local_path):
            site_packages_paths.append(local_path)
    
    # 가상환경 경로 추가
    venv_path = os.path.join(home, 'autobot_env', 'lib')
    if os.path.exists(venv_path):
        for item in os.listdir(venv_path):
            if item.startswith('python'):
                venv_site_pkg = os.path.join(venv_path, item, 'site-packages')
                if os.path.exists(venv_site_pkg):
                    site_packages_paths.append(venv_site_pkg)
    
    # 모든 경로에서 squeeze_pro.py 찾기
    fixed = False
    for site_pkg in site_packages_paths:
        squeeze_path = os.path.join(site_pkg, 'pandas_ta', 'momentum', 'squeeze_pro.py')
        if os.path.exists(squeeze_path):
            print(f"파일 발견: {squeeze_path}")
            # 파일 내용 읽기
            with open(squeeze_path, 'r') as f:
                content = f.read()
            
            # 내용 수정
            if 'from numpy import NaN as npNaN' in content:
                print(f"NaN 임포트 찾음, 수정 중...")
                fixed_content = content.replace('from numpy import NaN as npNaN', 'from numpy import nan as npNaN')
                
                # 수정된 내용 저장
                with open(squeeze_path, 'w') as f:
                    f.write(fixed_content)
                
                print(f"파일 수정 완료: {squeeze_path}")
                fixed = True
    
    if fixed:
        print("모든 수정 완료! 이제 ec2_hawkes_live.py 스크립트를 실행할 수 있습니다.")
        return True
    else:
        print("수정할 파일을 찾지 못했습니다.")
        return False

if __name__ == "__main__":
    fix_pandas_ta()