$(document).ready(function() {

    // event listener for send button
    $("#send-btn").click(function() {
        var user_input = $("#user-input").val();
        if (user_input != "") {
            $("#chat-output").append("<p class='user-msg'>" + user_input + "</p>");
            $("#user-input").val("");
            scrollToBottom();
            $.ajax({
                url: "/query",
                method: "POST",
                data: {
                    user_input: user_input
                },
								success: function(response) {
								    $("#chat-output").append("<p class='bot-msg'>" + response + "</p>");
								    scrollToBottom();
								}
            });
        }
    });

    // function to scroll chat window
    function scrollToBottom() {
        $(".chat-output").scrollTop($(".chat-output")[0].scrollHeight);
    }
}); // add this closing curly brace
