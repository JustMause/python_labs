a = ("Иванов Иван Иванович", "BIVT-25", 4.6)
def format_record(rec):
    fio, group, gpa = rec
    
    if not fio or not group:
        raise ValueError()
    
    if not isinstance(gpa, (int, float)):
        raise TypeError()
    
    fio_parts = fio.split()
    fio_clean = []
    for part in fio_parts:
        if part.strip():
            fio_clean.append(part.strip())
    
    if len(fio_clean) < 2:
        raise ValueError()
    
    surname = fio_clean[0]
    initials = ""
    for i in range(1, len(fio_clean)):
        if fio_clean[i]:
            initials += fio_clean[i][0].upper() + "."
    
    formatted_fio = surname.capitalize() + " " + initials
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{formatted_fio}, гр. {group}, GPA {formatted_gpa}"
