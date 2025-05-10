"""
This script directly fixes the specific pandas_ta file that has the import error
"""
import os

def fix_pandas_ta():
    # Path from the error message
    squeeze_pro_path = 'C:\\Users\\mycho\\AppData\\Roaming\\Python\\Python313\\site-packages\\pandas_ta\\momentum\\squeeze_pro.py'
    
    if not os.path.exists(squeeze_pro_path):
        print(f"Could not find the file: {squeeze_pro_path}")
        return False
    
    print(f"Found squeeze_pro.py at: {squeeze_pro_path}")
    
    # Read the file
    with open(squeeze_pro_path, 'r') as f:
        content = f.read()
    
    # Fix the import statement
    if 'from numpy import NaN as npNaN' in content:
        fixed_content = content.replace('from numpy import NaN as npNaN', 'from numpy import nan as npNaN')
        
        try:
            # Write the fixed content
            with open(squeeze_pro_path, 'w') as f:
                f.write(fixed_content)
            print(f"Successfully patched {squeeze_pro_path}")
            print("The 'NaN' import has been changed to 'nan' in the numpy import.")
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False
    else:
        print("The file does not contain the expected 'from numpy import NaN as npNaN' statement.")
        return False

if __name__ == "__main__":
    success = fix_pandas_ta()
    if success:
        print("Fix applied successfully. You can now run your script again.")
    else:
        print("Could not apply the fix. You may need to manually edit the file or run this script with administrator privileges.") 