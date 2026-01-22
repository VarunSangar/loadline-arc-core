from core.state import GlobalState

def get_state():
    return {
        "cognitive_load": GlobalState.cognitive_load,
        "task": GlobalState.current_task
    }
