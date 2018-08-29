function preparePicker() {
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false, // Close upon selecting a date,
    });
}

function setDueDate(dateString) {
    var due_date = Date.parse(dateString);
    $('#due_date').pickadate('picker').set('select', due_date, { format: 'dd/mm/yyyy' }).trigger('change');
}
