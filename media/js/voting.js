$(document).ready(function() {

    var $votingForms = $('#content form.vote');
    $votingForms.submit(function(ev) {
        var $form = $(this);
        ev.preventDefault();
        $.ajax({
            url: $form.attr('action'),
            type: "POST",
            data: $form.serialize(),
            dataType: 'json',
            success: function(data){
                $form.removeClass('changed');
            },
            error: function(XMLHttpRequest, textStatus, errorThrown){
                alert("Oops, there was an error, please try again... ");
            }
        });
       return false;
    });
    $votingForms.find('input[type="radio"]').change(function() {
        $(this).closest('form').addClass('changed');
    });

});