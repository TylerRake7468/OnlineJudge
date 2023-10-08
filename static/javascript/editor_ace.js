$(function create_editor() {
    $('textarea[data-editor]').each(function () {
        var textarea = $(this);
        var theme = textarea.data('editor');
        var editDiv = $('<div>', {
            position: 'absolute',
            width: '888px',
            height: '652px',
            'class': textarea.attr('class'),
            'id':'custom-editor'
        }).insertBefore(textarea);

        textarea.css('display', 'none'); // to avoid extra space below textarea
        ace.require("ace/ext/language_tools"); // language tools: brackets, tabs, indentations, etc
        var editor = ace.edit(editDiv[0]);

        var editor_mode = 'c_cpp';     

        editor.setOptions({
            enableBasicAutocompletion: true,
            enableSnippets: true,
            enableLiveAutocompletion: true, 
            showGutter: true, 
            showLineNumbers: true,
            fontSize: 17,
            theme: 'ace/theme/' + theme,
            mode: 'ace/mode/' + editor_mode,
            showPrintMargin: false,
        });

        editor.session.setValue(textarea.val());

        textarea.closest('form').submit(function () {
        textarea.val(editor.getSession().getValue());
        })
    });
});