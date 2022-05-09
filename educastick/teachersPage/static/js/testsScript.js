$(document).ready(function () {
  let groupsList = ['Группа 1', 'Группа 2']

  $('.element').click(function(){
    if ($(this).hasClass('active')){
      $(this).removeClass('active')
      $(this).next('.active_element').detach()
    } else{
      $(this).addClass('active')
      let element_id = $(this).attr('id')
      $(this).after(CreateTestAnswerBlock('Части речи', 'Глаголы', element_id))
    }
  })


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
})

function CreateTestAnswerBlock(module = '', theme = '', element_id){
  return $('<div class="active_element">\n' +
    '        <form action="" name="' + element_id + '">\n' +
    '        <div class="active_text">\n' +
    '          <p>Модуль: Части речи</p>\n' +
    '          <p>Тема: Глаголы</p>\n' +
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

function ElementSelectBlock(){
  return $('<div class="elements_choose">\n' +
    '            <input list="list_elements" class="find_element">\n' +
    '            <div class="close_choose" >X</div>     ' +
    '            <datalist id="list_elements">\n' +
    '            </datalist>\n' +
    '          </div>')
}

$(document).on('click','.close_choose', function(){
  $(this).parent().remove()
})






