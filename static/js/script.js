function main() {
    $.ajax({
        type: "GET",
        url: "/",
        data: {},
        success: function (response) {
            window.location.href = "/"
        }
    })
}

function map() {
    $.ajax({
        type: "GET",
        url: "/map",
        data: {},
        success: function (response) {
            window.location.href = "/map"
        }
    })
}

function board() {
    $.ajax({
        type: "GET",
        url: "/board",
        data: {},
        success: function (response) {
            window.location.href = "/board"
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
            window.location.href = "/login"
        }
    })
}

function signup() {
    $.ajax({
        type: "GET",
        url: "/login/signup",
        data: {},
        success: function (response) {
            window.location.href = "/login/signup"
        }
    })
}

function logout() {
    let date = new Date();
    date.setDate(date.getDate() - 100);
    let Cookie = `${name}=;Expires=${date.toUTCString()}`
    document.cookie = Cookie;

    alert('로그아웃!')
    window.location.href = "/login"
}