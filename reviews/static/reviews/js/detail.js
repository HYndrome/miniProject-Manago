const reviewLikeForm = document.querySelector('#review-like-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
reviewLikeForm.addEventListener('submit', function (event) {
  event.preventDefault()
  const restaurantId = event.target.dataset.restaurantId
  const reviewId = event.target.dataset.reviewId
  axios({
    method: 'post',
    url: `/reviews/${restaurantId}/${reviewId}/likes/`,
    headers: {'X-CSRFToken': csrftoken},
  })
  .then((response) => {
    const isLiked = response.data.is_liked
    const reviewLikeBtnIcon = document.querySelector('#review-like-form > button[type=submit] > i')
    
    if (isLiked === true) {
      reviewLikeBtnIcon.classList.remove('bi-heart')
      reviewLikeBtnIcon.classList.add('bi-heart-fill')
    } else {
      reviewLikeBtnIcon.classList.remove('bi-heart-fill')
      reviewLikeBtnIcon.classList.add('bi-heart')
    }
    
    const reviewLikeCountTag = document.querySelector('#review-like-count')
    const reviewLikeCountData = response.data.review_like_count
    reviewLikeCountTag.textContent = reviewLikeCountData
  })
  .catch((error) => {
    console.log(error.response)
  })
})



const commentUpdate = document.querySelectorAll('.comment-edit-btn')

commentUpdate.forEach(function (comment) {
  comment.addEventListener('click', function (event) {
    event.preventDefault()
    const commentId = event.target.dataset.commentId
    const commentUpdateDiv = document.querySelector(`#comment-edit-form-${commentId}`)
    const contentAreaText = commentUpdateDiv.querySelector(`#comment-edit-form-${commentId}>div>textarea`)
    commentUpdateDiv.hidden = false
    contentAreaText.textContent = document.querySelector(`#comment-content-${commentId}`).textContent
  })
})

const commentUpdateConfirms = document.querySelectorAll('.comment-edit-form')

commentUpdateConfirms.forEach(function (updateBtn) {
  updateBtn.addEventListener('submit', function (event) {
    event.preventDefault()
    const reviewId = event.target.dataset.reviewId
    const commentId = event.target.dataset.commentId
    const restaurantId = event.target.dataset.restaurantId
    const data = {
      content: document.querySelector(`#comment-edit-form-${commentId}>div>textarea`).value,
    }
    axios({
      method: 'post',
      url: `/reviews/${restaurantId}/${reviewId}/comments/${commentId}/update/`,
      headers: {'X-CSRFToken': csrftoken},
      data: JSON.stringify(data),
    })
    .then((response) => {
      updateBtn.hidden = true
      document.querySelector(`#comment-content-${commentId}`).textContent = data['content']
    })
    .catch((error) => {
      console.log(error.response)
    })
  })
})

const commentUpdateCancels = document.querySelectorAll('.comment-edit-form>div>.cancel')
commentUpdateCancels.forEach(function (cancelBtn) {
  cancelBtn.addEventListener('click', (event) => {
    const commentId = event.target.dataset.commentId
    const commentUpdateForm = document.querySelector(`#comment-edit-form-${commentId}`)
    commentUpdateForm.hidden = true
  })
})