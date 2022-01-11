function main() {
    $.ajax({
        type: "GET",
        url: "/",
        data: {},
        success: function (response) {
            location.href = "/"
        }
    })
}

function map() {
    $.ajax({
        type: "GET",
        url: "/map",
        data: {},
        success: function (response) {
            location.href = "/map"
        }
    })
}

function board() {
    $.ajax({
        type: "GET",
        url: "/board",
        data: {},
        success: function (response) {
            location.href = "/board"
        }
    })
}

function mypage() {
    $.ajax({
        type: "GET",
        url: "/mypage",
        data: {},
        success: function (response) {
            location.href = "/mypage"
        }
    })
}

function login() {
    $.ajax({
        type: "GET",
        url: "/login",
        data: {},
        success: function (response) {
            location.href = "/login"
        }
    })
}

function signup() {
    $.ajax({
        type: "GET",
        url: "/signup",
        data: {},
        success: function (response) {
            location.href = "/signup"
        }
    })
}

function duplicationCheck(inputID) {
    $.ajax({
        type: "POST",
        url: "/signup/idcheck",
        data: {id_give: inputID},
        success: function (response) {
            console.log(response["msg"])
        }
    })
}