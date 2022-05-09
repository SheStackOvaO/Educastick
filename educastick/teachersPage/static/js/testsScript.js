function MakeBlockActive(){
  let element_id = $(this).attr('id')
  if ($(this).hasClass('active')){
      $(this).removeClass('active')
      $(this).next('.active_element').detach()
    } else{
      $(this).addClass('active')
      $(this).after(CreateTestActiveBlock('Части речи', 'Глаголы'))
    }
}

function AddAnswersButton(){
   let element_id = $(this).parents('.element').attr('id')
    if ($(this).parents('.element').hasClass('active')){
      $(this).parents('.element').next('.active_element').detach()
      $(this).parents('.element').after(CreateTestAnswerBlock('Части речи', 'Глаголы', element_id))
    } else{
      $(this).parents('.element').addClass('active')
      //console.log(element_id)
      $(this).parents('.element').after(CreateTestAnswerBlock('Части речи', 'Глаголы', element_id))
    }
}

function CreateTestAnswerBlock(module = '', theme = '', element_id){
    let imgSrc = $('#hidden_goBackImg').attr('src')
  return $('<div class="active_element">\n' +
    '        <button class="go_back_button"><img src="' + imgSrc + '" alt="" class="plus"></button>' +
    '        <form action="" name="' + element_id + '">\n' +
    '        <div class="active_text">\n' +
    '          <p>Модуль: ' + module + '</p>\n' +
    '          <p>Тема: ' + theme + '</p>\n' +
    '        </div>\n' +
    '        <div class="select_element">\n' +
    '          <div class="element_add active_group_choose">\n' +
    '            Выбор группы\n' +
    '          </div>\n' +
    '        </div>\n' +
    '        <div class="active_butts">\n' +
    '          <input type="date" class="download_button">\n' +
    '          <input type="file" name="" id="" class="download_button">\n' +
    '          <button class="download_button" id="save_answer" type="submit">\n' +
    '            Сохранить ответы\n' +
    '          </button>\n' +
    '        </div>\n' +
    '        </form>\n' +
    '      </div>')
}

function CreateTestActiveBlock(module = '', theme = ''){
  return $('<div class="active_element">\n' +
      '  <a href="" class="statistic_href">Статистика</a>\n' +
      '        <div class="active_text">\n' +
      '          <p>Модуль: ' + module + '</p>\n' +
      '          <p>Тема: ' + theme + '</p>\n' +
      '          <p>Вопросы:</p>\n' +
      '          <ol>\n' +
      '            <li><p>Вопрос</p><p>Ответ: </p></li>\n' +
      '            <li><p>Вопрос</p><p>Ответ: </p></li>\n' +
      '          </ol>\n' +
      '        </div>\n' +
      '      </div>')
}

function ElementSelectBlock(){
  return $('<div class="elements_choose">\n' +
    '            <input list="list_elements" class="find_element">\n' +
    '            <div class="close_choose" >X</div>     ' +
    '            <datalist id="list_elements">\n' +
    '            </datalist>\n' +
    '          </div>')
}


$(document).ready(function () {
  let groupsList = ['Группа 1', 'Группа 2']

  $('.element').click(MakeBlockActive)

  $('.crud_but').click(function (){
    event.stopPropagation()
  })

  $('.add_answer_but').click(AddAnswersButton)

  $(document).on('click','.active_group_choose', function()
  {
      $(this).after(ElementSelectBlock())
      let datalist = document.querySelector('#list_elements')
        let datalist2 = $(this).siblings().children('#list_elements')
        console.log(datalist2)
        for(let i = 0; i < groupsList.length; i++)
        {
          let opt = groupsList[i]
          let el = document.createElement("option")
          el.value = opt
          datalist.appendChild(el)
        }
  })

    $(document).on('click','.close_choose', function(){
    $(this).parent().remove()
    })

    $(document).on('click','.go_back_button', function(){
        let parentElement = $(this).parents('.active_element').prev()
        $(this).parents('.active_element').detach()
        parentElement.after(CreateTestActiveBlock('Части речи', 'Глаголы'))
    })



})






