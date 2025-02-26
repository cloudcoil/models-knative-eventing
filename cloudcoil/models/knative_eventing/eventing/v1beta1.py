# Generated by cloudcoil-model-codegen v0.5.6
# DO NOT EDIT

from __future__ import annotations

from typing import (
    Annotated,
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    overload,
)

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import (
    BaseModel,
    BaseModelBuilder,
    BuilderContextBase,
    GenericListBuilder,
    ListBuilderContext,
    Never,
    Self,
)
from cloudcoil.resources import Resource


class Reference(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Reference"]:
            return Reference

        def build(self) -> "Reference":
            return Reference(**self._attrs)

        def api_version(self, value: Optional[str], /) -> Self:
            """
            API version of the referent.
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[str], /) -> Self:
            """
            Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        def name(self, value: Optional[str], /) -> Self:
            """
            Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
            """
            return self._set("name", value)

        def namespace(self, value: Optional[str], /) -> Self:
            """
            Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ This is an optional field, it gets defaulted to the object holding it if left out.
            """
            return self._set("namespace", value)

        def address(self, value: Optional[str], /) -> Self:
            """
            Address points to a specific Address Name
            """
            return self._set("address", value)

    class BuilderContext(BuilderContextBase["Reference.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Reference.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Reference."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Reference", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Reference.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[str], Field(alias="apiVersion")] = None
    """
    API version of the referent.
    """
    kind: Optional[str] = None
    """
    Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: Optional[str] = None
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    namespace: Optional[str] = None
    """
    Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ This is an optional field, it gets defaulted to the object holding it if left out.
    """
    address: Optional[str] = None
    """
    Address points to a specific Address Name
    """


class EventTypeSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EventTypeSpec"]:
            return EventTypeSpec

        def build(self) -> "EventTypeSpec":
            return EventTypeSpec(**self._attrs)

        def broker(self, value: Optional[str], /) -> Self:
            return self._set("broker", value)

        @overload
        def reference(
            self, value_or_callback: Optional[Reference], /
        ) -> "EventTypeSpec.Builder": ...

        @overload
        def reference(
            self,
            value_or_callback: Callable[[Reference.Builder], Reference.Builder | Reference],
            /,
        ) -> "EventTypeSpec.Builder": ...

        @overload
        def reference(self, value_or_callback: Never = ...) -> "Reference.BuilderContext": ...

        def reference(self, value_or_callback=None, /):
            """
            Reference a resource. For example, Broker.
            """
            if self._in_context and value_or_callback is None:
                context = Reference.BuilderContext()
                context._parent_builder = self
                context._field_name = "reference"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Reference.builder())
                if isinstance(output, Reference.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("reference", value)

        def description(self, value: Optional[str], /) -> Self:
            """
            Description is an optional field used to describe the EventType, in any meaningful way.
            """
            return self._set("description", value)

        def schema_(self, value: Optional[str], /) -> Self:
            """
            Schema is a URI, it represents the CloudEvents schemaurl extension attribute. It may be a JSON schema, a protobuf schema, etc. It is optional.
            """
            return self._set("schema_", value)

        def schema_data(self, value: Optional[str], /) -> Self:
            """
            SchemaData allows the CloudEvents schema to be stored directly in the EventType. Content is dependent on the encoding. Optional attribute. The contents are not validated or manipulated by the system.
            """
            return self._set("schema_data", value)

        def source(self, value: Optional[str], /) -> Self:
            """
            Source is a URI, it represents the CloudEvents source.
            """
            return self._set("source", value)

        def type(self, value: Optional[str], /) -> Self:
            """
            Type represents the CloudEvents type. It is authoritative.
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["EventTypeSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EventTypeSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EventTypeSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EventTypeSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EventTypeSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    broker: Optional[str] = None
    reference: Optional[Reference] = None
    """
    Reference a resource. For example, Broker.
    """
    description: Optional[str] = None
    """
    Description is an optional field used to describe the EventType, in any meaningful way.
    """
    schema_: Annotated[Optional[str], Field(alias="schema")] = None
    """
    Schema is a URI, it represents the CloudEvents schemaurl extension attribute. It may be a JSON schema, a protobuf schema, etc. It is optional.
    """
    schema_data: Annotated[Optional[str], Field(alias="schemaData")] = None
    """
    SchemaData allows the CloudEvents schema to be stored directly in the EventType. Content is dependent on the encoding. Optional attribute. The contents are not validated or manipulated by the system.
    """
    source: Optional[str] = None
    """
    Source is a URI, it represents the CloudEvents source.
    """
    type: Optional[str] = None
    """
    Type represents the CloudEvents type. It is authoritative.
    """


class Condition(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Condition"]:
            return Condition

        def build(self) -> "Condition":
            return Condition(**self._attrs)

        def last_transition_time(self, value: Optional[str], /) -> Self:
            """
            LastTransitionTime is the last time the condition transitioned from one status to another. We use VolatileTime in place of metav1.Time to exclude this from creating equality.Semantic differences (all other things held constant).
            """
            return self._set("last_transition_time", value)

        def message(self, value: Optional[str], /) -> Self:
            """
            A human readable message indicating details about the transition.
            """
            return self._set("message", value)

        def reason(self, value: Optional[str], /) -> Self:
            """
            The reason for the condition's last transition.
            """
            return self._set("reason", value)

        def severity(self, value: Optional[str], /) -> Self:
            """
            Severity with which to treat failures of this type of condition. When this is not specified, it defaults to Error.
            """
            return self._set("severity", value)

        def status(self, value: str, /) -> Self:
            """
            Status of the condition, one of True, False, Unknown.
            """
            return self._set("status", value)

        def type(self, value: str, /) -> Self:
            """
            Type of condition.
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["Condition.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Condition.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Condition."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Condition", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Condition.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    last_transition_time: Annotated[Optional[str], Field(alias="lastTransitionTime")] = None
    """
    LastTransitionTime is the last time the condition transitioned from one status to another. We use VolatileTime in place of metav1.Time to exclude this from creating equality.Semantic differences (all other things held constant).
    """
    message: Optional[str] = None
    """
    A human readable message indicating details about the transition.
    """
    reason: Optional[str] = None
    """
    The reason for the condition's last transition.
    """
    severity: Optional[str] = None
    """
    Severity with which to treat failures of this type of condition. When this is not specified, it defaults to Error.
    """
    status: str
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: str
    """
    Type of condition.
    """


class EventTypeStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EventTypeStatus"]:
            return EventTypeStatus

        def build(self) -> "EventTypeStatus":
            return EventTypeStatus(**self._attrs)

        def annotations(self, value: Optional[Dict[str, Any]], /) -> Self:
            """
            Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards.
            """
            return self._set("annotations", value)

        @overload
        def conditions(
            self, value_or_callback: List[Condition], /
        ) -> "EventTypeStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[Condition, Condition.Builder]],
                GenericListBuilder[Condition, Condition.Builder] | List[Condition],
            ],
            /,
        ) -> "EventTypeStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[Condition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            """
            Conditions the latest available observations of a resource's current state.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[Condition.Builder]()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Condition.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

        def observed_generation(self, value: Optional[int], /) -> Self:
            """
            ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.
            """
            return self._set("observed_generation", value)

    class BuilderContext(BuilderContextBase["EventTypeStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EventTypeStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EventTypeStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EventTypeStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EventTypeStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    annotations: Optional[Dict[str, Any]] = None
    """
    Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards.
    """
    conditions: Optional[List[Condition]] = None
    """
    Conditions the latest available observations of a resource's current state.
    """
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration")] = None
    """
    ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.
    """


class EventType(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EventType"]:
            return EventType

        def build(self) -> "EventType":
            return EventType(**self._attrs)

        @overload
        def spec(self, value_or_callback: Optional[EventTypeSpec], /) -> "EventType.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [EventTypeSpec.Builder], EventTypeSpec.Builder | EventTypeSpec
            ],
            /,
        ) -> "EventType.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "EventTypeSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = EventTypeSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(EventTypeSpec.builder())
                if isinstance(output, EventTypeSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: Optional[EventTypeStatus], /
        ) -> "EventType.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [EventTypeStatus.Builder], EventTypeStatus.Builder | EventTypeStatus
            ],
            /,
        ) -> "EventType.Builder": ...

        @overload
        def status(self, value_or_callback: Never = ...) -> "EventTypeStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = EventTypeStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(EventTypeStatus.builder())
                if isinstance(output, EventTypeStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

        def api_version(self, value: Optional[Literal["eventing.knative.dev/v1beta1"]], /) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["EventType"]], /) -> Self:
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "EventType.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "EventType.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = apimachinery.ObjectMeta.BuilderContext()
                context._parent_builder = self
                context._field_name = "metadata"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.ObjectMeta.builder())
                if isinstance(output, apimachinery.ObjectMeta.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("metadata", value)

    class BuilderContext(BuilderContextBase["EventType.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EventType.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EventType."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EventType", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EventType.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    spec: Optional[EventTypeSpec] = None
    status: Optional[EventTypeStatus] = None
    api_version: Annotated[
        Optional[Literal["eventing.knative.dev/v1beta1"]], Field(alias="apiVersion")
    ] = "eventing.knative.dev/v1beta1"
    kind: Optional[Literal["EventType"]] = "EventType"
    metadata: Optional[apimachinery.ObjectMeta] = None
