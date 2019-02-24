from PyFlow.Packages.BasePackage.Nodes.switchOnString import switchOnString
from PyFlow.Packages.BasePackage.Nodes.implicitPinCall import implicitPinCall
from PyFlow.Packages.BasePackage.Nodes.sequence import sequence
from PyFlow.Packages.BasePackage.UI.UISwitchOnStringNode import UISwitchOnString
from PyFlow.Packages.BasePackage.UI.UIImplicitPinCallNode import UIImplicitPinCall
from PyFlow.Packages.BasePackage.UI.UISequenceNode import UISequenceNode
from PyFlow.UI.UINodeBase import UINodeBase


def createUINode(raw_instance):
    if isinstance(raw_instance, switchOnString):
        return UISwitchOnString(raw_instance)
    if isinstance(raw_instance, implicitPinCall):
        return UIImplicitPinCall(raw_instance)
    if isinstance(raw_instance, sequence):
        return UISequenceNode(raw_instance)
    return UINodeBase(raw_instance)
