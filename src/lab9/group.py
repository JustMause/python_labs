import csv
from pathlib import Path
from models import Student
import sys
from typing import List
sys.path.append(r"C:\Users\Home\lab_python\lab_python-2\src")
class Group():
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding='utf-8')
        if not self.path.read_text(encoding='utf-8').split('\n')[0] == 'fio,birthdate,group,gpa':
            raise ValueError('Не корректный заголовок')
        with open(self.path, 'r', encoding='utf-8') as f:
            rd = list(csv.DictReader(f))
            [Student.from_dict(st) for st in rd]

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write('fio,birthdate,group,gpa\n')

    def _read_all(self) -> List[dict]:
        self._ensure_storage_exists()
        with open(self.path, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def list(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            rd = csv.reader(f)
            next(rd)
            Students = list(rd)
        return Students
    
    def _write_all(self, Students: List[dict]):
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(Students)

    def add(self, Student: Student):
        rows = self._read_all()
        if any(row['fio'] == Student.fio for row in rows):
            raise ValueError(f"Студент {Student.fio} уже существует")
        rows.append({
            'fio': Student.fio,
            'birthdate': Student.birthdate,
            'group': Student.group,
            'gpa': str(Student.gpa)
        })
        self._write_all(rows)
    

    def find(self, substr: str):
        with open(self.path, 'r', encoding='utf-8') as f:
            rd = list(csv.DictReader(f))
        return [Student.from_dict(r) for r in rd if substr in r['fio']]
    
    def remove(self, fio: str):
        with open(self.path, 'r', encoding='utf-8') as f:
            rd = csv.DictReader(f)
            data_new = [r for r in rd if fio not in r['fio']]
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            wr = csv.DictWriter(f, fieldnames=list(data_new[0].keys()))
            wr.writeheader()
            wr.writerows(data_new)

    def update(self, fio: str, **fields):
        data = Student.from_dict({'fio': fio, **fields}).to_dict()
        data.pop('fio')
        with open(self.path, 'r', encoding='utf-8') as f:
            rd = list(csv.DictReader(f))
            for r in rd:
                if fio in r['fio']:
                    r.update(data)
                    break 
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            wr = csv.DictWriter(f, fieldnames=list(rd[0].keys()))
            wr.writeheader()
            wr.writerows(rd)
    
if __name__ == "__main__":
     group = Group(r'C:\Users\Home\lab_python\lab_python-2\data\students.csv')
