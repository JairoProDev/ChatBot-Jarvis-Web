$(document).ready(function() {
    $('#sendbutton').click(function() {
        var userinput = $('#userinput').val();

        $.ajax({
            url: 'http://localhost:5000/get_response',
            type: 'post',
            dataType: 'json',
            contentType: 'application/json',
            success: function (data) {
                $('#chatbox').append('<p>Usuario: ' + userinput + '</p>');
                $('#chatbox').append('<p>Chatbot: ' + data.response + '</p>');
                $('#userinput').val('');
            },
            data: JSON.stringify({ "user_input": userinput })
        });
    });
});