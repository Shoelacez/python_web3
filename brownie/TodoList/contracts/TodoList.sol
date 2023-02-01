// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ToDo{
    // events
    event createdSuccesfully(address user, string task, string message);
    event updatedSuccesfully(address user, string task, string message);
    struct Task{
        string task;
        bool complete;
    }

    Task[] public tasks;

    // create a to-do list
    function createTask(string memory _task) public {
        Task memory task = Task(_task, false);
        tasks.push(task);
        emit createdSuccesfully(msg.sender, _task, "Task created succesfully");
    }

    // Update the to do list
    function updateTask(uint _at, string memory _updatedTask) public{
        tasks[_at].task = _updatedTask;
        emit updatedSuccesfully(msg.sender, _updatedTask, "Updated the task succesfully");
    }

    // Delete a task
    function deleteTask(uint _at) public {
        delete tasks[_at].task;
    }

    // toggle task
    function toggleComplete(uint _at) public {
       tasks[_at].complete = ! tasks[_at].complete;
    }
}


