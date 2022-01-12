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

function openClose() {
    // id 값 post-box의 display 값이 flex 이면(= 눈에 보이면)
    if ($('#post-box').css('display') == 'flex') {
        // post-box를 가리고
        $('#post-box').css('display', 'none');
    } else {
        // 아니면(눈에 보이지 않으면) post-box를 펴라
        $('#post-box').css('display', '');
        // 다시 버튼을 클릭하면, 박스 닫기를 할 수 있게 텍스트 바꿔두기
    }
}

function writeReview() {
    let id = $('#user_id').val()
    let rating = $('#rating').val()
    let review = $('#review').val()
    let title = $('#title').text()
    $.ajax({
        type: "POST",
        url: "/writeBoard",
        data: {
            id_give: id, rating_give: rating,
            review_give: review, title_give: title,
        },
        success: function (response) { // 성공하면
            if (response["result"] == "success") {
                window.location.reload()
            }
        }
    })
}

function showreview(num) {
    let title = $('#title').text()
    $.ajax({
        type: "GET",
        url: "/readBoard",
        data: {'title': title},
        success: function (response) {
            if (response["result"] == "success") {
                    let review = response['review_list'][num]
                    let id_rec = review['id']
                    let rating_rec = review['rating']
                    let review_rec = review['review']
                    let html = `<div class="row g-3 board_wrap">
    <div class="col-md-6">
        <label for="user_id" class="form-label">아이디</label>
        <p class="board_border" style="width: 200px"> ${id_rec} </p>
    </div>
    <div class="col-md-6">
        <label for="rating" class="form-label">평점</label>
        <p class="board_border" style="width: 50px"> ${rating_rec} </p>
    </div>
    <div class="col-12">
        <label for="review" class="form-label">리뷰</label>
        <p class="board_border" > ${review_rec}
        <p/>
    </div>
</div>
                                    `
                    $('#add_review').append(html)
                }


        }
    })
}

function showClass() {
    $.ajax({
        type: 'GET',
        url: '/readList',
        data: {},
        success: function (response) {
            if (response['result'] == 'success') {
                let classlist = response['class_list']
                $('#star-box').empty()
                for (let i = 0; i < classlist.length; i++) {
                    let list = classlist[i]
                    let temphtml = `<div class="card mb-3" style="max-width: 540px;">
<div class="row g-0">
    <div class="col-md-4">
      <img src="${list['img_url']}" class="img-fluid rounded-start cat" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <a href="${list['url']}" class="card-title">${list['title']}</a>
        <p class="card-text">${list['text']}</p>
        <p class="card-text"><small class="text-muted">평점 : ${list['aver']}</small></p>
        <a href="/board?title=${list['title']}">리뷰보러가기</a>
        <br>
      </div>
    </div>
  </div>
</div>`
                    $('#class-box').append(temphtml)
                }
            }
        }
    });
}