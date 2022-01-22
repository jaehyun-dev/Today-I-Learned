# 2022.01.22 토요일

JQuery를 이용한 첫 번째 기능

```JavaScript
<script>
        function openclose() {
            let status = $('#post-box').css('display');
            console.log(status);
            if (status == 'block') {
                $('#post-box').hide();
                $('#btn-posting-box').text('포스팅박스 열기');
            } else{
                $('#post-box').show();
                $('#btn-posting-box').text('포스팅박스 닫기');
            }
        }
</script>
```
포스팅박스가 열려있으면 버튼 이름을 '포스팅박스 닫기'로 변경.   
버튼을 클릭하면 포스팅박스가 닫히며 버튼 이름이 '포스팅박스 열기'로 변경.
