<script>
var options = {
    key: "rzp_live_RPQOT0nooNjHJv",   // ⚠️ Use rzp_test_ on localhost
    amount: 50000,                  // amount in paise
    currency: "INR",
    name: "GreatKart",
    description: "Order Payment",
    handler: function (response) {
        alert("Payment Successful");
        console.log(response.razorpay_payment_id);
    }
};

var rzp1 = new Razorpay(options);
document.getElementById("pay-btn").onclick = function (e) {
    rzp1.open();
    e.preventDefault();
};
</script>
