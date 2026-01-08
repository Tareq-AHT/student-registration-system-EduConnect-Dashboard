# Project Documentation: Edu-Connect Dashboard
**Platform:** Django Web Framework  
**Category:** Education Management & Enrollment System  

---

## 1. Project Overview
Edu-Connect Dashboard is a modern Learning Management System (LMS) designed to streamline the course enrollment process. Students can browse available courses, add them to a dynamic cart, and complete their enrollment through a secure checkout simulation. The system includes a robust backend for administrators to manage students, courses, and financial records.

---

## 2. Database Schema (Backend Models)
The project utilizes a relational database structure with three core models. Below are the visual representations of the database tables:

### A. Student Table
Manages the identity of users within the platform.
* **Fields:** `Name`, `Email`, `Password`.
![Student Table](db_screenshots/student_table.png)

### B. Course Table
The repository for all educational offerings.
* **Fields:** `Name`, `Price`, `Duration`, `Instructor`.
![Course Table](db_screenshots/course_table.png)

### C. Enrollment Table
A comprehensive log of all financial transactions and course sign-ups.
* **Fields:** `Student Name`, `Selected Courses`, `Total Amount`, `Payment Method`, `Timestamp (Date & Time)`.
![Enrollment Table](db_screenshots/enrollment_table.png)

---

## 3. Key Technical Implementations

### Backend Logic (models.py)
The core data structure is defined using Django Models to ensure data integrity.
```python
class Enrollment(models.Model):
    student_name = models.CharField(max_length=255)
    courses = models.TextField() 
    payment_method = models.CharField(max_length=50, default="bkash")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.student_name} - {self.timestamp.date()}" ```

### Backend Logic (models.py)
The core data structure is defined using Django Models to ensure data integrity.
```def save_enrollment(request):
    if request.method == "POST":
        s_name = request.POST.get('student_name')
        c_names = request.POST.get('course_names')
        p_method = request.POST.get('payment_method')
        t_price = request.POST.get('total_price')

        Enrollment.objects.create(
            student_name=s_name,
            courses=c_names,
            payment_method=p_method,
            total_amount=t_price
        )
        return redirect('enrolled_list')```

### Frontend Calculations (JavaScript)
I implemented real-time price calculation to enhance user experience.
``` function updateCart() {
    let total = 0;
    let selectedCourses = [];
    document.querySelectorAll('.course-checkbox:checked').forEach(cb => {
        total += parseFloat(cb.dataset.price);
        selectedCourses.push(cb.dataset.name);
    });
    document.getElementById('totalPrice').innerText = total;
    document.getElementById('modalPrice').innerText = total;
    document.getElementById('hiddenTotalPrice').value = total;
}```

### 4. Edu-Connect Dashboard: Pros & Limitations

### ✅ Pros:
- Real-time Calculation:** The cart totals are updated instantly via JavaScript without needing a page refresh.
- Detailed Reporting:** The Enrolled List table provides a professional breakdown of transactions, including exact dates and times.
- Automated Admin Interface:** Customized Django Admin panel allows for efficient data filtering, searching, and management using `list_display` and `search_fields`.
- Modern UI/UX:** A dark-themed, glossy interface using linear gradients and Poppins typography provides a premium user experience.
- Data Integrity:** Hidden input fields and server-side redirects ensure that the calculated amounts on the frontend are accurately passed to the backend.

#### ❌ Limitations:
- Payment Gateway Integration:** Currently uses a manual payment recording system (Simulation); it lacks integration with live gateways like Stripe or SSLCommerz.
- Password Security:** Passwords are saved in plain text for this prototype; a production environment would require Django’s built-in PBKDF2 hashing.
- Static Media Handling:** Course thumbnails and instructor photos are currently static; dynamic media upload functionality is not yet implemented.
- Student Session:** While students can register, the system does not yet feature a unique logged-in "Student Dashboard" or session-based authentication for the checkout.

---

### 5. Conclusion
Edu-Connect Dashboard serves as a powerful **Minimum Viable Product (MVP)**. It successfully automates the enrollment workflow for educational institutions. Future iterations will focus on implementing automated payment APIs, encrypted authentication systems, and a dedicated student portal.
