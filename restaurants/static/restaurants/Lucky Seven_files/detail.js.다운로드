const form = document.querySelector('#wish-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
form.addEventListener('submit', function (event) {
  event.preventDefault()
  const restaurantId = event.target.dataset.restaurantId
  axios({
    method: 'post',
    url: `/restaurants/${restaurantId}/wish/`,
    headers: {'X-CSRFToken': csrftoken},
  })
    .then((response) => {
      const isWished = response.data.is_wished
      const wishBtn = document.querySelector('#wish-form > button[type=submit] > i')
      if (isWished === true) {
        wishBtn.classList.add('bi-star-fill')
        wishBtn.classList.remove('bi-star')
      } else {
        wishBtn.classList.remove('bi-star-fill')
        wishBtn.classList.add('bi-star')
      }
      const wishCountTag = document.querySelector('#wish-count')
      const wishCountData = response.data.wish_count
      wishCountTag.textContent = wishCountData
    })
})

