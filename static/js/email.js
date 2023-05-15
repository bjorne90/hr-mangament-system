function sendEmail() {
    // Fetch the user's email address and other necessary data
    var userEmail = 'user@example.com';
    var shiftDetails = 'Shift details...';
  
    // Prepare the email parameters
    var templateParams = {
      to_email: userEmail,
      message: shiftDetails
    };
  
    // Send the email using EmailJS
    emailjs.send('service_219mi6n', 'template_nip32wo', templateParams)
      .then(function(response) {
        console.log('Email sent successfully!', response);
      }, function(error) {
        console.error('Error sending email:', error);
      });
  }
  