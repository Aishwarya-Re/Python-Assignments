$(document).ready(function(){
    $('#form').submit(function(e){
        var memberArr = [];
        $('.member_data').each(function(){
            var thisMember = {};
            $(this).children().each(function(){
                thisMember[$(this).attr('name')] = $(this).val();
            });
            memberArr.push(thisMember);
            // Delete this input
            $(this).remove();
        });

        var input = $("<input>").attr("type", "hidden").attr("name", "members").val(JSON.stringify(memberArr));
        $('#dynamic_form').append($(input));
        e.preventDefault();

        $.post("http://geraintanderson.com/cgi-bin/ajax_array.py",
        $('#form').serialize(),
        function(data, status){
            $('#member_info').html(data);
            // Reset the form
            $('#dynamic_form').html('<span class="member_data"><input type="text" name="name"><input type="text" name="date"></span><br>');
        });
    });

    function add_contact() {
        // $('#contact').submit(function(){
            // Add new form fields
            $('#contact_div').append($('.contact_form'));
    }
        // })};

    function add_address() {
        // $('#address').submit(function(){
            // Add new form fields
            $('#address_div').append($('.address_form'));
    }
        // })};
});
function add_contact() {
    // $('#contact').submit(function(){
        // Add new form fields
        $('#contact_div').append($('.contact_form'));
}
