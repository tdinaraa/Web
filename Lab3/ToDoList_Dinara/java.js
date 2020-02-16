var addTask = document.getElementById("AddTask"); //AddTask->for button
var tasks = document.getElementById("container"); //container->list
var tasksNum = 0;

console.log(tasks);

addTask.addEventListener('click', addTaskClicked); //when we press (click) the buttom we call the function addTaskClicked

function addTaskClicked() 
{
    tasksNum++;
    var el = document.createElement('div'); //seperate elements 
    var btn = document.createElement('button');
    var checkbox = document.createElement('input');
    var taskName = document.getElementById('TaskName').value || ("New Task");
    if(taskName === "New Task")
    {
        let res = confirm("Create new task default name \"New Task\"?");
        if(res === false)
        {
            return;
        }
    }
    document.getElementById('TaskName').value = null;

    el.id = "id" + tasksNum;
    el.classList.add('div', 'undone');

    btn.innerHTML='delete';
    btn.addEventListener('click', deleteTaskClicked);
    btn.myParam = el.id;
    btn.classList.add('btn');
    
    checkbox.type = 'checkbox';
    checkbox.classList.add('checkbox');
    checkbox.addEventListener('change', (event) => 
    {
        if (event.target.checked)
        {
            console.log('checked');
            checkbox.parentElement.classList.remove('undone');
            checkbox.parentElement.classList.add('done');
        } 
        else 
        {
            console.log('not checked');
            checkbox.parentElement.classList.remove('done');
            checkbox.parentElement.classList.add('undone');
        }
      });

    el.innerHTML = taskName;
    el.prepend(checkbox);
    el.append(btn);

    tasks.append(el);
    console.log(tasks);
}

function deleteTaskClicked(id) 
{
    console.log(id.target.myParam);
    document.getElementById(id.target.myParam).remove();
}
