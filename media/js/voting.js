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
                $form.find(".stars").css('opacity', '1');
            },
            error: function(XMLHttpRequest, textStatus, errorThrown){
                alert("Oops, there was an error, please try again... ");
            }
        });
       return false;
    });
    $votingForms.find('.stars input[type="radio"]').click(function() {
        var $form = $(this).parents("form");
        $form.find(".stars").attr('class', 'stars stars-' + $(this).val());
        $form.find(".stars").css('opacity', '.2');
        $form.submit();
    });
});