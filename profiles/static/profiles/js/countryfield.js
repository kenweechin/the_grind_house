// Get the country field value when the page first load
// It then store in a variable
let countrySelected = $('#id_default_country').val();
// if country selected if false, set element color to '#aab7c4'
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
// Capture the change event by 
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});