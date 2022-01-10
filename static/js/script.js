function main() {
    $.ajax({
        type: "GET",
        url: "/",
        data: {},
        success: function (response) {
            location.replace("/")
        }
    })
}

function map() {
    $.ajax({
        type: "GET",
        url: "/map",
        data: {},
        success: function (response) {
            location.replace("/map")
        }
    })
}
function board() {
    $.ajax({
        type: "GET",
        url: "/board",
        data: {},
        success: function (response) {
            location.replace("/board")
        }
    })
}
function mypage() {
    $.ajax({
        type: "GET",
        url: "/mypage",
        data: {},
        success: function (response) {
            location.replace("/mypage")
        }
    })
}
function login() {
    $.ajax({
        type: "GET",
        url: "/login",
        data: {},
        success: function (response) {
            location.replace("/login")
        }
    })
}
function signup() {
    $.ajax({
        type: "GET",
        url: "/signup",
        data: {},
        success: function (response) {
            location.replace("/signup")
        }
    })
}