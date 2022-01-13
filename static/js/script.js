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
    if (id == '' || review == '') {
        alert('입력을 확인해주세요!')
        return
    }
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


function updateReview(id) {
    let update_review = prompt("리뷰를 수정해주세요")
    {
        $.ajax({
            type: "POST",
            url: "/updateBoard",
            data: {
                id_give: id,
                review_give: update_review,
            },
            success: function (response) { // 성공하면
                if (response["result"] == "success") {
                    window.location.reload()
                }
            }
        })
    }

}

function deleteReview(id) {
    if (confirm("리뷰를 삭제하시겠습니까?") == true) {
        $.ajax({
            type: "POST",
            url: "/deleteBoard",
            data: {
                id_give: id
            },
            success: function (response) { // 성공하면
                if (response["result"] == "success") {
                    window.location.reload()
                }
            }
        })
    }

}

function showReview(num) {
    let title = $('#title').text()
    $.ajax({
        type: "GET",
        url: "/readBoard",
        data: {'title': title},
        success: function (response) {
            if (response["result"] == "success") {
                let sec_id = response['sec_id'][num]['_id']
                let review = response['review_list'][num]
                let id_rec = review['id']
                let rating_rec = review['rating']
                let review_rec = review['review']
                let html = `<div class="row g-3 board_wrap font3">
    <div class="col-md-6">
        <p style="width: 200px">아이디 : ${id_rec} </p>
    </div>
    <div class="col-md-3">
        
        <p  style="width: 100px"> 평점 : ${rating_rec}/5 </p>
    </div>
    <div class="col-md-2">
    <button class="btn btn-outline-dark btn-sm font1" onclick="updateReview('${sec_id}')">수정</button> 
     &nbsp&nbsp&nbsp
    <button class="btn btn-outline-dark btn-sm font1" onclick="deleteReview('${sec_id}')">삭제</button>
    </div>
    <div class="col-12">
        <label for="review" class="form-label font1">리뷰</label>
        <p class="border border-1" > ${review_rec}
        <p/>
        
    </div>
</div>
<br>
                                    `
                $('#add_review').append(html)
            }


        }
    })
}

function showClass(num) {
    $.ajax({
        type: 'GET',
        url: '/readClass',
        data: {},
        success: function (response) {
            if (response['result'] == 'success') {
                let classlist = response['class_list']
                let list = classlist[num]
                let temphtml = `<div class="card mb-3 class-card font1 " style="border-radius: 12px">
<div class="row g-0 align-left" >
    <div class="col-md-4">
    <a href="${list['url']}">
    <img src="${list['img_url']}" class="img-fluid rounded-start img_px" alt="...">   
</a>
       </div>
    <div class="col-md-8">
      <div class="card-body">
        <p class="card-title" ><b>${list['title']}</b></p>
        <p><small class="card-text">${list['text']}</small></p>
        <div class="card-text"><small class="text-muted">평점 : ${list['aver']}</small></div>
        <button onclick="location.href='/boardclass?title=${list["title"]}'" class="font2 btn btn-outline-primary" style="font-size: 20px">리뷰보러가기</button>
        <br>
      </div>
    </div>
  </div>
</div>`
                $('#class-box').append(temphtml)
            } else {
                return 'a'
            }
        }

    });
}

function showAcademy(num) {
    $.ajax({
        type: 'GET',
        url: '/readAcademy',
        data: {},
        success: function (response) {
            if (response['result'] == 'success') {
                let academylist = response['academy_list']
                let list = academylist[num]
                let tempimg;
                if (!list['imgsrc']){
                    tempimg = '../static/rtan.png'
                }
                else {
                    tempimg = list['imgsrc']
                }

                let temphtml = `<div class="card mb-3 class-card font1 " style="border-radius: 12px">
<div class="row g-0 align-left" >
    <div class="col-md-4">
    <img src="${tempimg}" class="img-fluid rounded-start img_px" alt="...">   
       </div>
    <div class="col-md-8">
      <div class="card-body">
        <p class="card-title" ><b>${list['name']}</b></p>
        <p><small class="card-text">${list['address']}</small></p>
        <div class="card-text"><small class="text-muted">평점 : ${list['aver']}</small></div>
        <button onclick="location.href='/boardacademy?title=${list["name"]}'" class="font2 btn btn-outline-primary" style="font-size: 20px">리뷰보러가기</button>
        <br>
      </div>
    </div>
  </div>
</div>`
                $('#class-box').append(temphtml)
            } else {
                return 'a'
            }
        }

    });
}