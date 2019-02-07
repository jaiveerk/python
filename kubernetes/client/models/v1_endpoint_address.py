# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1EndpointAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hostname': 'str',
        'ip': 'str',
        'node_name': 'str',
        'target_ref': 'V1ObjectReference'
    }

    attribute_map = {
        'hostname': 'hostname',
        'ip': 'ip',
        'node_name': 'nodeName',
        'target_ref': 'targetRef'
    }

    def __init__(self, hostname=None, ip=None, node_name=None, target_ref=None):
        """
        V1EndpointAddress - a model defined in Swagger
        """

        self._hostname = None
        self._ip = None
        self._node_name = None
        self._target_ref = None
        self.discriminator = None

        if hostname is not None:
          self.hostname = hostname
        self.ip = ip
        if node_name is not None:
          self.node_name = node_name
        if target_ref is not None:
          self.target_ref = target_ref

    @property
    def hostname(self):
        """
        Gets the hostname of this V1EndpointAddress.
        The Hostname of this endpoint

        :return: The hostname of this V1EndpointAddress.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this V1EndpointAddress.
        The Hostname of this endpoint

        :param hostname: The hostname of this V1EndpointAddress.
        :type: str
        """

        self._hostname = hostname

    @property
    def ip(self):
        """
        Gets the ip of this V1EndpointAddress.
        The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.

        :return: The ip of this V1EndpointAddress.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this V1EndpointAddress.
        The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.

        :param ip: The ip of this V1EndpointAddress.
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")

        self._ip = ip

    @property
    def node_name(self):
        """
        Gets the node_name of this V1EndpointAddress.
        Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.

        :return: The node_name of this V1EndpointAddress.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this V1EndpointAddress.
        Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.

        :param node_name: The node_name of this V1EndpointAddress.
        :type: str
        """

        self._node_name = node_name

    @property
    def target_ref(self):
        """
        Gets the target_ref of this V1EndpointAddress.
        Reference to object providing the endpoint.

        :return: The target_ref of this V1EndpointAddress.
        :rtype: V1ObjectReference
        """
        return self._target_ref

    @target_ref.setter
    def target_ref(self, target_ref):
        """
        Sets the target_ref of this V1EndpointAddress.
        Reference to object providing the endpoint.

        :param target_ref: The target_ref of this V1EndpointAddress.
        :type: V1ObjectReference
        """

        self._target_ref = target_ref

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1EndpointAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
