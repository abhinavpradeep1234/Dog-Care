$(document).ready(function() {
    // This code will run once the page (DOM) is fully loaded
    // alert('Page is loaded!');

$(".payWithRazorpay").click(function(e) {
    e.preventDefault();
    var quantity =$("[name='quantity']").val();
    var email =$("[name='email']").val();
    var address =$("[name='address']").val();
    var payement_mode =$("[name='payement_mode']").val();
    if (quantity == '' || email == '' || address == '' || payement_mode == '') {
        // alert('All fields are required');
        Swal.fire({
            title: "Warning",
            text: "All fields are required",
            icon: "warning",
          });
        return false;
    }
    else{
    $.ajax({
        method:"GET",
        url: "/proceed-to-pay/",
       
        success: function(response){
            console.log(response);
        },
    })
        



        // var options = {
        //     "key": "YOUR_KEY_ID", // Enter the Key ID generated from the Dashboard
        //     "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
        //     "currency": "INR",
        //     "name": "Acme Corp", //your business name
        //     "description": "Test Transaction",
        //     "image": "https://example.com/your_logo",
        //     "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
        //     "handler": function (response){
        //         alert(response.razorpay_payment_id);
        //         alert(response.razorpay_order_id);
        //         alert(response.razorpay_signature)
        //     },
        //     "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
        //         "name": "Gaurav Kumar", //your customer's name
        //         "email": "gaurav.kumar@example.com", 
        //         "contact": "9000090000"  //Provide the customer's phone number for better conversion rates 
        //     },
        //     "notes": {
        //         "address": "Razorpay Corporate Office"
        //     },
        //     "theme": {
        //         "color": "#3399cc"
        //     }
        // };
        // var rzp1 = new Razorpay(options);
        // rzp1.open();
    }



    // rzp1.on('payment.failed', function (response){
    //         alert(response.error.code);
    //         alert(response.error.description);
    //         alert(response.error.source);
    //         alert(response.error.step);
    //         alert(response.error.reason);
    //         alert(response.error.metadata.order_id);
    //         alert(response.error.metadata.payment_id);
    // });
    
});




    
});
