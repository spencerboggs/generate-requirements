# Generate Requirements
A python script that automatically generates requirments.txt files based on the imports in your python files.

```
git clone https://github.com/spencerboggs/generate-requirements.git
cd generate-requirements
pip install -r requirements.txt
```

### Example Usage:

Generate a requirements.txt file for the specified folder that contains all requirements for that folder and its subfolders.
```
python main.py \folder\
```

Generate a requirements.txt file that contains all of the requirements, including standard libraries that are typically installed with python.
```
python main.py \folder\ -a
```

Generate a requirements.txt file file for each folder in the specified directory including the top folder.
```
python main.py \folder\ -r
```

Generate a requirements.txt file file for each folder in the specified directory including the top folder and include standard libraies.
```
python main.py \folder\ -r -a
```
