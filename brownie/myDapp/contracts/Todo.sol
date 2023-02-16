// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ToDo{

    struct Task{
        uint id;
        uint date;
        string task;
        string author;
        bool complete;
    }

    Task[] tasks;

    // Creating a task
    function createTask(string memory _task, string memory _author) public{
        tasks.push(Task(tasks.length, block.timestamp, _task, _author, false));
    }

    // get a task
    function getTask(uint id) public view returns(uint , uint , string memory ,string memory, bool ){
        return (
            id,
            tasks[id].date,
            tasks[id].task,
            tasks[id].author,
            tasks[id].complete
        );
    }

    function allTasks() public view returns (Task[] memory){
        return tasks;
    }
}