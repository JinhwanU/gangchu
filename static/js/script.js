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
        url: "/login/signup",
        data: {},
        success: function (response) {
            location.href = "/login/signup"
            // 회원가입 버튼을 눌렀을 때 login.html에 login_form='signup' 변수를 보내고 불러오기
        }
    })
}
