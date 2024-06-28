import smtplib
import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def _get_connection(self):
        # Create a new SSL context that does not verify certificates
        context = ssl._create_unverified_context()
        # Use the context in the SMTP connection
        self.connection = smtplib.SMTP(self.host, self.port, local_hostname=self.local_hostname, timeout=self.timeout)
        if self.use_tls:
            self.connection.starttls(context=context)
        if self.username and self.password:
            self.connection.login(self.username, self.password)
        return self.connection
