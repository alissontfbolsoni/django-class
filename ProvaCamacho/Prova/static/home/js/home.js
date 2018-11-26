function showLoading() {
 

    $('#btn-submit').trigger('click')

    if ($('.field-validation-error').find('span').length == 0) {
        $('#loading').removeClass('none')
        $('body').addClass('body-overflow')
        window.scrollTo(0, 0);
    }
}


