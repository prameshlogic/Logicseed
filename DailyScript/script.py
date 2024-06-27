
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fpdf import FPDF

# Step 1: Import Data
data = pd.read_csv('data.csv')

# Step 2: Process Data
data.dropna(inplace=True)
data['date'] = pd.to_datetime(data['date'])
daily_data = data[data['date'] == pd.Timestamp('today').normalize()]

# Step 3: Generate Report
plt.figure(figsize=(10, 6))
sns.countplot(data=daily_data, x='category')
plt.title('Daily Report')
plt.xlabel('Category')
plt.ylabel('Count')
plt.savefig('daily_report.png')

# Step 4: Create PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Daily Report', 0, 1, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()
    
    def add_plot(self, image_path):
        self.image(image_path, x=10, y=None, w=190)

pdf = PDF()
pdf.add_page()
pdf.chapter_title('Summary')
pdf.chapter_body('This is the summary of the daily report.')
pdf.chapter_title('Plot')
pdf.add_plot('daily_report.png')
pdf.output('daily_report.pdf')

# Step 5: Send Email
def send_email(report_path, recipient_email):
    from_email = "your_email@example.com"
    password = "your_password"
    to_email = recipient_email

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Report"

    with open(report_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={report_path}')
        msg.attach(part)

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

send_email('daily_report.pdf', 'recipient@example.com')
