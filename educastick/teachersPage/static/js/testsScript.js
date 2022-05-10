function MakeBlockActive() {
    let element_id = $(this).attr('id')
    if ($(this).hasClass('active')) {
        $(this).removeClass('active')
        $(this).next('.active_element').detach()
    } else {
        $(this).addClass('active')
        $(this).after(CreateTestActiveBlock('Части речи', 'Глаголы'))
    }
}

function AddAnswersButton() {
    let element_id = $(this).parents('.element').attr('id')
    if ($(this).parents('.element').hasClass('active')) {
        $(this).parents('.element').next('.active_element').detach()
        $(this).parents('.element').after(CreateTestAnswerBlock('Части речи', 'Глаголы', element_id))
    } else {
        $(this).parents('.element').addClass('active')
        //console.log(element_id)
        $(this).parents('.element').after(CreateTestAnswerBlock('Части речи', 'Глаголы', element_id))
    }
}

function EditButton() {
    let element_id = $(this).parents('.element').attr('id')
    if ($(this).parents('.element').hasClass('active')) {
        $(this).parents('.element').next('.active_element').detach()
        $(this).parents('.element').after(CreateEditTestBlock)
    } else {
        $(this).parents('.element').addClass('active')
        $(this).parents('.element').after(CreateEditTestBlock)
    }
}

function CreateEditTestBlock(){
    let goBackImgSrc = $('#hidden_goBackImg').attr('src')
    let plusImgSrc = $('#hidden_plusImg').attr('src')
    let deleteImgSrc = $('#hidden_deleteImg').attr('src')
    return $('<div class="active_element">\n' +
        '        <button class="go_back_button"><img src="' + goBackImgSrc + '" alt="" class="plus"></button>' +
        '                <div class="active_text">\n' +
        '                    <p><label>Модуль:\n' +
        '                        <input type="text" name="moduleInput" class="input_text">\n' +
        '                    </label></p>\n' +
        '                    <p><label>Тема:\n' +
        '                        <input type="text" name="themeInput" class="input_text">\n' +
        '                    </label></p>\n' +
        '                    <p>Вопросы:</p>\n' +
        '                    <ol>\n' +
        '                        <li class="question_answer">\n' +
        '                            <p>\n' +
        '                                <input type="text" name="1" class="input_text">\n' +
        '                            </p>\n' +
        '                            <p>\n' +
        '                                <label>Правильный ответ:\n' +
        '                                    <input type="text" name="1_1" class="input_text">\n' +
        '                                </label>\n' +
        '                            </p>\n' +
        '                            <p class="variant_answer">\n' +
        '                                <label>Вариант ответа:\n' +
        '                                    <input type="text" name="1_2" class="input_text">\n' +
        '                                </label>\n' +
        '                            </p>\n' +
        '                        </li>\n' +
        '<div>' +
        '                             <button class="new_question_answer_button"><img src="'+plusImgSrc+'" alt="" class="crud_but_img"></button>\n' +
        '                             <button class="delete_question_answer_button"><img src="'+deleteImgSrc+'" alt="" class="crud_but_img"></button>\n' +
        '</div>' +
        '                        <li class="question_answer">\n' +
        '                            <p>\n' +
        '                                <input type="text" name="2" class="input_text">\n' +
        '                            </p>\n' +
        '                            <p>\n' +
        '                                <label>Правильный ответ:\n' +
        '                                    <input type="text" name="2_1" class="input_text">\n' +
        '                                </label>\n' +
        '                            </p>\n' +
        '                        </li>\n' +
        '<div>' +
        '                             <button class="new_question_answer_button"><img src="'+plusImgSrc+'" alt="" class="crud_but_img"></button>\n' +
        '                             <button class="delete_question_answer_button"><img src="'+deleteImgSrc+'" alt="" class="crud_but_img"></button>\n' +
        '</div>' +
        '                    </ol>\n' +
        '                </div>\n' +
        '                <div class="edit_buttons">\n' +
        '                    <button class="new_question_button"><img src="'+plusImgSrc+'" alt="" class="crud_but_img"></button>\n' +
        '                    <button class="save_button">Сохранить</button>\n' +
        '                </div>\n' +
        '            </div>')
}

function CreateTestAnswerBlock(module = '', theme = '', element_id) {
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

function CreateTestActiveBlock(module = '', theme = '') {
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

function ElementSelectBlock() {
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

    $('.crud_but').click(function () {
        event.stopPropagation()
    })

    $('.add_answer_but').click(AddAnswersButton)

    $('.edit_but').click(EditButton)

    $(document).on('click', '.new_question_answer_button', function () {
        $(this).parent().prev('.question_answer').append($('<p class="variant_answer">\n' +
            '                                <label>Вариант ответа:\n' +
            '                                    <input type="text" name="1_2" class="input_text">\n' +
            '                                </label>\n' +
            '                            </p>'))
    })

    $(document).on('click', '.delete_question_answer_button', function () {
        $(this).parent().prev('.question_answer').children('.variant_answer:last').remove()
    })

    $(document).on('click', '.active_group_choose', function () {
        $(this).after(ElementSelectBlock())
        let datalist = document.querySelector('#list_elements')
        let datalist2 = $(this).siblings().children('#list_elements')
        console.log(datalist2)
        for (let i = 0; i < groupsList.length; i++) {
            let opt = groupsList[i]
            let el = document.createElement("option")
            el.value = opt
            datalist.appendChild(el)
        }
    })

    $(document).on('click', '.close_choose', function () {
        $(this).parent().remove()
    })

    $(document).on('click', '.go_back_button', function () {
        let parentElement = $(this).parents('.active_element').prev()
        $(this).parents('.active_element').detach()
        parentElement.after(CreateTestActiveBlock('Части речи', 'Глаголы'))
    })


})






