task TaskA:
    class : redbreast.core.spec.StartTask
end

task TaskB:
    class : redbreast.core.spec.SimpleTask
end

task TaskC(TaskB):
end

task TaskD(TaskB):
end

task TaskE(TaskB):
end

task TaskF(TaskB):
end

task TaskG:
    class : redbreast.core.spec.JoinTask
end

task TaskH:
    class : redbreast.core.spec.EndTask
end

process TestWorkflow:
    '''
    desc This is a small workflow definination for testing.
    '''
    key : value
    
    tasks:
        TaskA as A
        TaskB as B
        TaskC as C
        TaskD as D
        TaskE as E
        TaskF as F
        TaskG as G
        TaskH as H
    end
    
    flows:
        A->B->C->G->H
        A->D->E->F->G
    end
    
    code A.ready:
        if data.get("is_superuser") == True:
        	return Task('B')
        else:
        	return Task('task1')
    end
    
    code B.ready:
        return Task('task1')
    end
end
